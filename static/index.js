const muteBtn = document.getElementById("toggle-mic-btn");

const micOnSvg = document.getElementById("mic-on");
const micOffSvg = document.getElementById("mic-off");

// This is the mic state
let isMicMuted = null;

const handleToggle = () => {
    if (isMicMuted) {
        muteBtn.classList.add("pressed");
        micOffSvg.style.display = "block";
        micOnSvg.style.display = "none";
    } else {
        muteBtn.classList.remove("pressed");
        micOffSvg.style.display = "none";
        micOnSvg.style.display = "block";
    }
}

addEventListener("load", async () => {
    const res = await fetch("/mic/is_muted");
    isMicMuted = await res.json();
    handleToggle();
});

muteBtn.onclick = () => {
    fetch("/mic/toggle", { method: "POST" });
    isMicMuted = !isMicMuted;
    handleToggle();
}
