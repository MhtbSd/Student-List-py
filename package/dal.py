

from typing import Literal
from os.path import isfile


# region Save
def save_dal(file_path: str, content: str | list[str], mode: Literal["a", "w"] = "a", write_state: Literal["wr", "wl"] = "wr"):

    try:
        file_object = open(file=file_path, mode=mode)

        if write_state == "wr":
            file_object.write(content)
            
        elif write_state == "wl":
            file_object.writelines(content)

    except BaseException as err:
        return ("ERROR", err)

    else:
        return ("SUCCESS", None)

    finally:
        if "file_object" in locals() and not file_object.closed:
            file_object.close()
# endregion Save


# region Read
def read_dal(file_path):

    if not isfile(file_path):

        try:
            file_object = open(file=file_path, mode="x")

        except BaseException as err:
            return ("ERROR", err)
        
        else:
            return ("SUCCESS", [])
        
        finally:
            if "file_object" in locals() and not file_object.closed:
                file_object.close()

    try:
        file_object = open(file=file_path)
        res = file_object.readlines()

    except BaseException as err:
        return ("ERROR", err)
    
    else:
        return ("SUCCESS", res)
    
    finally:
        if "file_object" in locals() and not file_object.closed:
            file_object.close()
# endregion Read
