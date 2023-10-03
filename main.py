from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
from mic import Mic

app = FastAPI()


@app.get("/mic/is_muted")
def read_root():
    return mic.is_muted

@app.post("/mic/toggle")
def mute_or_unmute_mic():
    mic.toggle()

app.mount("/", StaticFiles(directory="static",html = True), name="static")


def get_user_input():
    is_muted = input("Is the mic currently muted? (y/n)\n")
    if is_muted.lower() == "y":
        return True
    elif is_muted.lower() == "n":
        return False
    else:
        print('Invalid input (only "y" and "n" are valid). Please try again.')
        return get_user_input()

if __name__ == '__main__':
    IS_MUTED = get_user_input()
    mic = Mic(IS_MUTED)
    uvicorn.run(app, host='0.0.0.0', port=8000)
