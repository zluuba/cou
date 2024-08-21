from tqdm.asyncio import tqdm


def get_progress_bar(length):
    """
    Creates a progress bar for file processing.

    Args:
        length (int): The total number of items to process.

    Returns:
        tqdm: A tqdm progress bar instance.
    """

    return tqdm(
        total=length,
        desc='Processing files',
        unit='file',
        bar_format='{l_bar}{bar} | {n_fmt}/{total_fmt} '
                   '[{elapsed}<{remaining}, {rate_fmt}{postfix}]'
    )
