def total_calc(bill_amount, tip_perc):
    """This is an example of positional arguments"""
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")

total_calc(150, 20)