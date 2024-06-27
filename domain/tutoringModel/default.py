class DefaultAlgorithm:
    def __init__(self, default_learning_path: list[dict]):
        self.default_learning_path = default_learning_path

    def get_learning_path(self, list_of_le: list) -> str:
        # Get all classifications from list of le
        classifications = [le["classification"] for le in list_of_le]

        # Filter the default learning by classification and sort it afterwards by pos
        filtered_sorted_path = sorted(
            (
                element
                for element in self.default_learning_path
                if element["classification"] in classifications
            ),
            key=lambda x: x["position"],
        )

        # Update positions
        for index, element in enumerate(filtered_sorted_path):
            element["position"] = index + 1

        # Return classifications as string
        return ", ".join(element["classification"] for element in filtered_sorted_path)
