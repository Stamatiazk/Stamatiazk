#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class InvestmentAdvisor:
    def __init__(self):
        self.preferences = {}

    def get_user_preferences(self):
        self.preferences['age'] = int(input("Παρακαλώ εισάγετε την ηλικία σας: "))
        self.preferences['investment_goal'] = input("Ποιος είναι ο στόχος των επενδύσεων σας (συνταξιοδότηση, απόκτηση περιουσίας, άλλο): ")
        self.preferences['risk_tolerance'] = input("Ποια είναι η ανοχή σας στον κίνδυνο (χαμηλή, μέτρια, υψηλή): ")
        self.preferences['investment_duration'] = int(input("Για πόσα χρόνια σκοπεύετε να επενδύσετε: "))

    def suggest_portfolio(self):
        age = self.preferences['age']
        risk_tolerance = self.preferences['risk_tolerance']
        duration = self.preferences['investment_duration']

        if age < 35 and risk_tolerance == 'υψηλή' and duration > 10:
            return "Προτείνεται ένα ανάλογο χαρτοφυλάκιο με 70% μετοχές, 20% ομόλογα, 10% εναλλακτικές επενδύσεις."
        elif age >= 35 and risk_tolerance == 'μέτρια':
            return "Προτείνεται ένα ανάλογο χαρτοφυλάκιο με 50% μετοχές, 40% ομόλογα, 10% εναλλακτικές επενδύσεις."
        else:
            return "Προτείνεται ένα συντηρητικό χαρτοφυλάκιο με 20% μετοχές, 70% ομόλογα, 10% εναλλακτικές επενδύσεις."


advisor = InvestmentAdvisor()
advisor.get_user_preferences()
portfolio = advisor.suggest_portfolio()
print(portfolio)


# In[ ]:




