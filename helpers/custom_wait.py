class AttributeHasValue:

    def __init__(self, locator, attribute_name, attribute_value):
        self.locator = locator
        self.attribute_name = attribute_name
        self.attribute_value = attribute_value
        pass

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if self.attribute_value in element.get_attribute(self.attribute_name):
            return element
        else:
            raise Exception(f"Attribute: {self.attribute_name} has not value: {self.attribute_value}")


class AttributeHasText:

    def __init__(self, locator, attribute_name, attribute_text):
        self.locator = locator
        self.attribute_name = attribute_name
        self.attribute_text = attribute_text
        pass

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if self.attribute_text in element.text:
            return element
        else:
            raise Exception(f"{self.attribute_name} has no text: {self.attribute_text}")


