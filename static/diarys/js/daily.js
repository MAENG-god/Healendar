var move_next = document.querySelector('.move_next');
move_next.addEventListener("click", function(){
    location.href = "/diarys/" + String(next_year) + "/" + String(next_month) + "/" + String(next_date)
})

var move_prev = document.querySelector('.move_prev');
move_prev.addEventListener("click", function(){
    location.href = "/diarys/" + String(prev_year) + "/" + String(prev_month) + "/" + String(prev_date)
})

function add_routine(){
    var exercise = document.createElement("div");
    exercise.className = "routine_name";
    exercise.innerHTML = `
    <span style="display:flex; margin: 0 0 0 15%;">Name:<input class="input_name" name="Name" type="text"></span>
    <span style="display:flex; margin: 0 0 0 15%;"> Sets:<input class="input_sets" name="sets" type="number" min="1"></span>
    <input class="input_go large_go" type="submit" value="GO!">
    `;
    var parent = document.querySelector(".add_table");
    if(parent.style.display == "flex"){
        
    }
    else{
        parent.style.display = "flex";
        parent.appendChild(exercise);
    }
}

var go_home = document.querySelector('.home');
go_home.addEventListener("click", function(){
    location.href = "/diarys/"
})

function edit_routine(e){
    var parent = e.parentNode;
    while (parent.hasChildNodes()) {
        parent.removeChild(parent.firstChild);
    }
    parent.innerHTML=`
    <button class="del_routine" type="button">DEL</button>
    <span><input class="edit_name" name="Name" type="text" placeholder="Name"></span>
    <span><input class="edit_sets" name="sets" type="number" min="1" placeholder="Sets"></span>
    <input type="submit" value="GO!">
    `
}
