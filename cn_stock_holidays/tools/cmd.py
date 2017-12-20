#coding: utf-8

import click
from cn_stock_holidays import data
from cn_stock_holidays import data_hk
import datetime
import platform


@click.command()
@click.option("--market", "-m", default='cn', help="CN or Hk")
@click.option("--start", "-s", required=True, help="START DATE FORMAT YYYY-MM-DD or YYYYMMDD")
@click.option("--end", "-e", required=True,  help="END DATE FORMAT YYYY-MM-DD or YYYYMMDD")
@click.option("--output", "-o", default="-", help="Output file, - is stdout")
@click.option("--format", "-f", default='YYYY-MM-DD', help="output format ,YYYY-MM-DD or YYYYMMDD")
@click.option("--daytype", "-d", default="workday", help="workday or holiday")
def main(market, start, end, output, format, daytype):
    if market == 'cn':
        holiday = data
    else:
        holiday = data_hk

    start_date = parse_date(start)
    end_date = parse_date(end)


    output_arr = []
    cur_date = start_date

    while cur_date < end_date:
        if holiday.is_trading_day(cur_date):
            if daytype == 'workday':
                output_arr.append(cur_date)
        else:
            if daytype == 'holiday':
                output_arr.append(cur_date)

        cur_date = cur_date + datetime.timedelta(days=1)

    linesep = "\n\r" if platform.system() == 'Windows' else "\n"

    if format == 'YYYY-MM-DD':
        format_str = "%Y-%m-%d"
    else:
        format_str = "%Y%m%d"

    output_str = linesep.join([d.strftime(format_str) for d in output_arr])


    if output == '-':
        print(output_str)
    else:
        with open(output, "w") as f:
            f.write(output_str)


def parse_date(dstr):

    # handle YYYYMMDD
    if len(dstr) == 8:
        return data.int_to_date(dstr)
    else:
        # handle YYYY-MM-DD
        darr = dstr.split("-")
        if len(darr) != 3:
            raise Exception("start or end format is invalid")

        return datetime.date(year=int(darr[0]), month=int(darr[1]), day=int(darr[2]))



if __name__ == '__main__':
    main()