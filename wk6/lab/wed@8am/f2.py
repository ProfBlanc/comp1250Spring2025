def purchase(payment_type: str, amount_due: float, amount_given:float=0.0):
    allowed_payment_types = "visa,debit,mastercard,cash".split(",")
    if isinstance(payment_type, str) and payment_type in allowed_payment_types and isinstance(amount_due, float) and isinstance(amount_given, float):
        
        if payment_type.lower() != allowed_payment_types[-1]:
            return {"change_owing": 0, "debited": amount_due, "result": "The transaction was complete", "card_type": payment_type}
        
        if amount_given < amount_due:
            return {"error": "You have insufficient funds for this purchase"}
        return {"change_owing": amount_given - amount_due, "debited": amount_due, "result": "The transaction was complete"}
    else:
        return {"error": "Incorrect paramaters used for this method"}


res = purchase("visa", 10.0)
print(res)
res = purchase("debit", 5.0)
print(res)
res = purchase("cash", 10.0)  # error message return expected
print(res)
res = purchase("cash", 8.0, 10.0)
print(res)
res = purchase("cash", 8.0, 1.0)
print(res)
