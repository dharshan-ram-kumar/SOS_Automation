from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction

def long_press(driver, element, duration=2):
    rect = element.rect
    x = rect["x"] + rect["width"] / 2
    y = rect["y"] + rect["height"] / 2

    finger = PointerInput(interaction.POINTER_TOUCH, "finger")

    actions = ActionBuilder(driver, mouse=finger)
    actions.pointer_action.move_to_location(int(x), int(y))
    actions.pointer_action.pointer_down()
    actions.pointer_action.pause(duration)  # hold
    actions.pointer_action.pointer_up()
    actions.perform()
