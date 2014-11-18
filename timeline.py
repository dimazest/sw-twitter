"""Timeline plot generator for tweet streams."""
from opster import command
import pandas as pd


@command()
def timeline(
    input_file,
    output=('o', 'timeline.png', 'The output file name.'),
):
    """Generate a timeline plot for a stream of tweets."""
    df = pd.read_csv(
        input_file,
        sep=' ',
        names=['Date', 'Count'],
        parse_dates=True,
        index_col='Date',
    )

    df.plot().get_figure().savefig(output)


if __name__ == '__main__':
    timeline.command()
