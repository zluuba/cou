from aiofiles import open as aiopen
from asyncio import gather, create_task, Semaphore
from os import walk, path as os_path
from pathlib import Path
from tqdm.asyncio import tqdm


async def get_files_to_count(path: Path) -> list:
    files_to_count = []

    if path.is_file():
        if path.suffix == '.py':
            files_to_count.append(path)
        return files_to_count

    for root, _, files in walk(path):
        for file in files:
            ext = Path(file).suffix

            if ext == '.py':
                full_path = os_path.join(root, file)
                files_to_count.append(full_path)

    return files_to_count


async def count_lines_in_file(file: os_path,
                              semaphore: Semaphore,
                              progress_bar: tqdm) -> int:
    async with semaphore:
        lines_count = 0

        async with aiopen(file, mode='r') as f:
            async for _ in f:
                lines_count += 1

        progress_bar.update(1)
        return lines_count


async def count_lines(raw_path: str,
                      concurrency_limit: int = 10) -> int:

    path = Path(raw_path).resolve()
    semaphore = Semaphore(concurrency_limit)
    files_to_count = await get_files_to_count(path)

    progress_bar = tqdm(
        total=len(files_to_count),
        desc='Processing files',
        unit='file',
    )

    tasks = [
        create_task(count_lines_in_file(filename, semaphore, progress_bar))
        for filename in files_to_count
    ]
    results = await gather(*tasks)

    progress_bar.close()

    return sum(results)
