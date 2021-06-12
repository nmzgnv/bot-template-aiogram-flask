const sureText = "Are you sure?";
const successText = "Success!";
const errorText = "Error";

$.get("/get_current_bot_token", (data) => {
    $("#tokenInputField").val(data.token);
});

const SendRequestIfConfirmed = (url) => {
    if (window.confirm(sureText)) {
        $.post(url, {})
            .done((data) => {
                alert(successText);
            })
            .fail(() => {
                alert(errorText);
            });
    }
}

$("#changeTokenButton").click(() => {
    if (window.confirm(sureText)) {
        let data = {token: $('#tokenInputField').val()};
        $.post("/change_token", data, () => {
            console.log(successText)
        })
            .done((data) => {
                alert("Token changed!");
            })
            .fail(() => {
                alert(errorText);
            });
    }
});

$("#stopBotButton").click(() => {
    SendRequestIfConfirmed("/stop_bot");
});

$("#restartBotButton").click(() => {
    SendRequestIfConfirmed("/restart_bot");
});