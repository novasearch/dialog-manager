from example.dialog_factory.dialog_elements import AbstractEvent


class SpecifyStepIntent(AbstractEvent):
    id = "SpecifyStepIntent"
    description = ""

    def __init__(self):
        pass

    @staticmethod
    def is_valid(state_manager: dict):
        return state_manager["intent"] == SpecifyStepIntent.id
