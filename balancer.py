TARGET_VAS_ALLOCATION = 0.2
TARGET_VGS_ALLOCATION = 0.8

print(f'Target VAS allocation: {TARGET_VAS_ALLOCATION * 100:.1f}%')
print(f'Target VGS allocation: {TARGET_VGS_ALLOCATION * 100:.1f}%')
print()

if TARGET_VAS_ALLOCATION + TARGET_VGS_ALLOCATION != 1:
    print('Error: target allocations must add to 100%')
    exit()


def input_cash_amount(prompt: str) -> float:
    while True:
        try:
            amount = float(input(prompt))
            rounded_amount = round(amount, 2)
            if amount != rounded_amount:
                print(f'Warning: rounded to ${rounded_amount}')
            return rounded_amount
        except ValueError:
            print('Error: please enter a valid number')


current_vas_value = input_cash_amount('Enter the current VAS value ($): ')
current_vgs_value = input_cash_amount('Enter the current VGS value ($): ')
print()

current_portfolio_value = current_vas_value + current_vgs_value
current_vas_allocation = current_vas_value / current_portfolio_value
current_vgs_allocation = current_vgs_value / current_portfolio_value
print(f'Current portfolio value: ${current_portfolio_value:.2f}')
print(f'Current VAS allocation: {current_vas_allocation * 100:.1f}%')
print(f'Current VGS allocation: {current_vgs_allocation * 100:.1f}%')
print()

total_investment_amount = input_cash_amount('Enter the total investment amount ($): ')
print()

future_portfolio_value = current_portfolio_value + total_investment_amount
vas_investment_amount = future_portfolio_value * TARGET_VAS_ALLOCATION - current_vas_value
vas_investment_amount = max(0, min(round(vas_investment_amount, 2), total_investment_amount))
vgs_investment_amount = total_investment_amount - vas_investment_amount
print(f'VAS investment amount: ${vas_investment_amount:.2f}')
print(f'VGS investment amount: ${vgs_investment_amount:.2f}')
