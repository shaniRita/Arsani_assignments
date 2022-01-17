async function get_user_backend() {
    let id = document.getElementById("backend_id_input").value
    user_data = await (await fetch("/assignment11/outer_source_backend?id=" + id)).json()
    insert_user_to_div(user_data, "backend_user_div")
}

async function get_user_frontend(){
    let id = document.getElementById("frontend_id_input").value
    response = await (await fetch('https://reqres.in/api/users/'+id)).json()
    insert_user_to_div(response.data, "frontend_user_div")
}

function insert_user_to_div(user_data, div) {
    const div_elem = document.getElementById(div);
    div_elem.innerHTML = "";
    const user_img = document.createElement("img")
    user_img.setAttribute("src", user_data['avatar']);
    const user_info = document.createElement("div")
    const id = document.createTextNode(`User ID: ${user_data.id}`)
    const email = document.createTextNode(`Email: ${user_data.email}`)
    const name = document.createTextNode(`Full Name: ${user_data.first_name} ${user_data.last_name}`)
    user_info.appendChild(id)
    user_info.appendChild(document.createElement("br"))
    user_info.appendChild(email)
    user_info.appendChild(document.createElement("br"))
    user_info.appendChild(name)
    user_info.appendChild(document.createElement("br"))
    div_elem.appendChild(user_info)
    div_elem.appendChild(user_img)
}