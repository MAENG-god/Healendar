let date = new Date();

const renderCalender = () => {
    const viewYear = date.getFullYear();
    const viewMonth = date.getMonth();

    document.querySelector('.year').textContent = `${viewYear}`;
    document.querySelector('.month').textContent = `${viewMonth + 1}`;

    const prevLast = new Date(viewYear, viewMonth, 0);
    const thisLast = new Date(viewYear, viewMonth + 1, 0);

    const PLDate = prevLast.getDate();
    const PLDay = prevLast.getDay();

    const TLDate = thisLast.getDate();
    const TLDay = thisLast.getDay();

    const prevDates = [];
    const thisDates = [...Array(TLDate + 1).keys()].slice(1);
    const nextDates = [];

    if (PLDay !== 6) {
        for (let i = 0; i < PLDay + 1; i++) {
            prevDates.unshift(PLDate - i);
        }
    }

    for (let i = 1; i < 7 - TLDay; i++) {
        nextDates.push(i);
    }

    const dates = prevDates.concat(thisDates, nextDates);
    const firstDateIndex = dates.indexOf(1);
    const lastDateIndex = dates.lastIndexOf(TLDate);

    dates.forEach((date, i) => {
        const condition = i >= firstDateIndex && i < lastDateIndex + 1 ?
            'this' :
            'other';
        // if(date == 7 & viewMonth == 3){
        //     dates[i] = `
        //         <div class="date ${condition}" onclick="date_btn(${date}, ${viewYear}, ${viewMonth})">
    
        //             <div class="date-itm">
        //                 ${date}
        //             </div>
    
    
        //             <div class="date_event">
        //                 <div class="event-itm">수너니 생일♥️</div>
        //             </div>
    
        //         </div>
        //     `;
        //     }
        if(condition == "this"){
        dates[i] = `
            <div class="date ${condition}" onclick="date_btn(${date}, ${viewYear}, ${viewMonth})">

                <div class="date-itm">
                    ${date}
                </div>


                <div class="date_event">
                    <div class="event-itm"></div>
                </div>

            </div>
        `;
        }
        else{
            dates[i] = `
            <div class="date ${condition}">

                <div class="date-itm">
                    ${date}
                </div>


                <div class="date_event">
                    <div class="event-itm"></div>
                </div>

            </div>
        `;
        }
    });

    document.querySelector('.dates').innerHTML = dates.join('');


    const today = new Date();
    if (viewMonth === today.getMonth() && viewYear === today.getFullYear()) {
        for (let date of document.querySelectorAll('.date-itm')) {
            if (+date.innerText === today.getDate()) {
                date.parentNode.classList.add('today');
                break;

            }
        }
    }
};

renderCalender();

const prevMonth = () => {
    date.setDate(1)
    date.setMonth(date.getMonth() - 1);
    renderCalender();
};

const nextMonth = () => {
    date.setDate(1)
    date.setMonth(date.getMonth() + 1);
    renderCalender();
};

const goToday = () => {
    date = new Date();
    renderCalender();
};

var today_workout = document.querySelector(".go_workout");
today_workout.addEventListener("click", function(){
    var now = new Date()
    var now_date = now.getDate()
    var now_year = now.getFullYear()
    var now_month = now.getMonth()
    date_btn(now_date, now_year, now_month)
});

function say_hi(text){
    alert("hi" + text)
}

function date_btn(date, year, month){
    location.href = "/diarys/" + String(year) + "/" + String(month + 1) + "/" + String(date)
}
