from tqdm.asyncio import tqdm


def get_progress_bar(length):
    return tqdm(
        total=length,
        desc='Processing files',
        unit='file',
    )
