from helper import Helper


class PoliciesPage(Helper):
    def add_policy(self, method, selector, method2="By.CSS_SELECTOR", selector2=".add"):
        self.wait_for_element_and_click(method2, selector2)
        self.wait_for_element_and_click(method, selector)
        