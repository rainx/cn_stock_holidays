#coding: utf-8

import click
from cn_stock_holidays.common import str_to_int, int_to_date

@click.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
def main(input, output):
    lines = [one.strip().replace("-", "") for one in input.readlines() if one.strip() != ""]
    lines = [one for one in lines if int_to_date(str_to_int(one)).weekday() < 5]
    output.write("\n".join(lines))
    # click.echo("Done! writing to output file!")

if __name__ == '__main__':
    main()