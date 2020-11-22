function validate()
{
    var email = document.getElementById("email");
    var user_name = document.getElementById("user_name");
    var pwd = document.getElementById("pwd");
    var first_name = document.getElementById("first_name");
    var last_name = document.getElementById("last_name");
    if (email.value =="" || user_name.value =="" || pwd.value =="" || last_name.value =="" || first_name.value =="")
    {
        alert("Each fields are required!!")
        return false;
    }
    else
    {
        return true;
    }
}

function login_validation() {
    var username = document.getElementById("username");
    var lpwd = document.getElementById("lpwd");
    if ( username.value =="" || lpwd.value =="")
    {
        alert("Each fields are required!!")
        return false;
    }
    else
    {
        return true;
    }

}