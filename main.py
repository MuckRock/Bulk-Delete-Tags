"""
This Add-On allows you to bulk delete tags and/or key value pairs from a set of documents. 
"""
import sys
from documentcloud.addon import AddOn


class BulkDeleteTags(AddOn):
    """DocumentCloud Add-On to bulk remove tags"""

    def main(self):
        """The main add-on functionality goes here."""
        # fetch your add-on specific data
        del_key = self.data.get("del_key")
        del_value = self.data.get("del_value")
        clear_all = self.data.get("clear_all", False)

        if del_value is not None and del_key != "_tag":
            self.set_message(
                "If you want to delete a tag, you must provide _tag as the key name"
            )

        if del_value is None and del_key == "_tag":
            if clear_all is True:
                self.set_message("Clearing all tags")
            else:
                self.set_message(
                    "You have selected _tag with no value specified. If you want to clear all tags, you must check the clear all box."
                )
                sys.exit(0)
        for document in self.get_documents():
            print(document.data)
            if del_key in document.data:
                if del_value is not None:
                    # Delete key-value pairs with matching value
                    document.data = {
                        k: v for k, v in document.data.items() if v != del_value
                    }
                else:
                    # Delete only the specified key
                    del document.data[del_key]
                document.put()


if __name__ == "__main__":
    BulkDeleteTags().main()
