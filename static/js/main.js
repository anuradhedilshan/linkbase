window.fbAsyncInit = function () {
    FB.init({
        appId: '2589928161224931',
        autoLogAppEvents: true,
        xfbml: true,
        version: 'v6.0'
    });
};




{

    let loginBtn = document.getElementById("loginBtn");
    let requestBtn = document.getElementById("requestBtn");
    let obj = document.getElementById("idIs");
    console.log(obj);

    if (obj != null) {
        {
            loginBtn.innerText = "logOut";
            loginBtn.classList.remove("btn-success");
            loginBtn.setAttribute("onclick", "submitForm.logOut()")
            loginBtn.classList.add("btn-danger");
        }
    }


}


function removeSearch(element) {
    const sr = document.getElementById("searchResult");
    sr.style.display = "none"

}

function search(i) {
    console.log("Clicked");

    val = i == null || i == "" ? null : i;
    console.log(val);
    const sr = document.getElementById("searchResult");
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = () => {
        if (xhttp.readyState == 4 && xhttp.status == 200) {
            response = JSON.parse(xhttp.response)
            sr.style.display = "block";
            sr.innerHTML = `<li class="list-group-item text-secondary">${response['error']}<button type="button" onclick="removeSearch()" class="close" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button></li>`
            if (response['is']) {
                for (i = 0; i < response['data'].length; i++) {
                    console.log(response['data'][i]);
                    let list = document.createElement("a");
                    list.className = "list-group-item";
                    list.setAttribute("href", `/view?id=${response['data'][i][0]}`);
                    list.setAttribute('target', 'blank');
                    list.innerText = response['data'][i][1];

                    sr.appendChild(list);

                }
            }



        }
    }

    xhttp.open("GET", `/search?val=${val} `);
    xhttp.send();

}


//hero box scroll


function slider(element) {
    const slider = element;
    let isDown = false;
    let startX;
    let scrollLeft;

    slider.addEventListener('mousedown', (e) => {
        isDown = true;
        slider.classList.add('active');
        startX = e.pageX - slider.offsetLeft;
        scrollLeft = slider.scrollLeft;
    });
    slider.addEventListener('mouseleave', () => {
        isDown = false;
        slider.classList.remove('active');
    });
    slider.addEventListener('mouseup', () => {
        isDown = false;
        slider.classList.remove('active');
    });
    slider.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - slider.offsetLeft;
        const walk = (x - startX) * 5; //scroll-fast
        slider.scrollLeft = scrollLeft - walk;

    });
}


//scroll event end















function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
} //get cokkies









class changeView {
    static data;
    modalBox = document.getElementById('modalBox');
    constructor(view) {


        switch (view.getAttribute('role')) {
            case 'request':
                this.getData('static/umsView/request.html');
                break;
            case 'signUp':
                this.getData('static/umsView/login.html');
                break;
            case 'signIn':
                this.getData('static/umsView/signin.html');
                break;

        }
    }


    getData(url) {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = () => {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
                this.modalBox.style.display = "block";
                this.modalBox.innerHTML = xhttp.response;
                console.warn('request reloding');
            }
        }

        xhttp.open("GET", url);
        xhttp.send();



    }
    static close() {
        modalBox.style.display = ' none';
        modalBox.innerHTML = "";
    }


    static selectOwn(view) {

        if (view.value == 1 || view.value == 2) {
            document.getElementById('ver').setAttribute('disabled', "");

        } else {
            document.getElementById('ver').removeAttribute('disabled', "");

        }

    } // end change view Class







} // changeView class




class submitForm {
    form;
    requestUrl;
    constructor(form, requestUrl) {
        this.form = form;
        this.requestUrl = requestUrl;
        var isVal = true;
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        console.log(forms, "sdsd");

        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function (form) {

            if (form.checkValidity() === false) {
                event.preventDefault();
                event.stopPropagation();
                isVal = false;
            }
            form.classList.add('was-validated');

        });
        console.log(isVal);
        if (isVal) {
            this.sendAjax();
        }





    }


    sendAjax() {
        var token = getCookie("csrftoken");
        let formData = new FormData();
        let data = this.form.getElementsByClassName('form-control');
        console.log(data);


        for (var i = 0; i < data.length; i++) {

            formData.append(data[i].getAttribute('id'), data[i].value);
            console.log(data[i]);


        }



        //STAIC ROOT

        let xhttp = new XMLHttpRequest();
        var a = document.getElementsByTagName("body");
        xhttp.onreadystatechange = () => {

            if (xhttp.readyState == 4 && xhttp.status == 200) {
                console.info('REQUEST  **sucsess** in main.js line-143');
                var jsonData = JSON.parse(xhttp.response);
                this.showMessages(jsonData);
                a[0].append(xhttp.response);

            } else {

                console.info("REQUEST **FAILD** in main.js line-151");
                a[0].append(xhttp.response)
            }

        }

        xhttp.open("post", this.requestUrl);
        xhttp.setRequestHeader("X-CSRFToken", token);
        xhttp.send(formData);


    }


    showMessages(jsonData) {
        let alertBox = document.getElementById("alertBox");
        console.log(jsonData['is']);
        alertBox.style.display = "none";
        var head = jsonData['is'] ? "congragulation" : "errors";
        var wclass = jsonData['is'] ? "alert-success" : "alert-danger";
        console.warn(jsonData['errors']);

        try {
            if (jsonData['request']) {
                setTimeout(() => {
                    document.getElementById("modalBox").style.display = "none"
                }, 2000);
            }
        } catch (error) {
            console.error("error in request");

        }

        let massage = `<strong>${head}</strong> ${jsonData['errors']}
        <button type='button' onClick="console.log(this)" class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button>`;
        alertBox.innerHTML = massage;
        alertBox.classList.add(wclass);
        alertBox.style.display = "block"
        console.log(alertBox.style.display);
        document.addEventListener('click', () => {
            alertBox.style.display = "none", console.log("click");
        });

        if (alertBox.style.display == "block") {

            setTimeout((e) => {
                alertBox.style.display = "none"
            }, 3000);


            console.log(jsonData);

        }

        if (jsonData['isLoged']) {
            setTimeout(() => {
                location.reload()
            }, 1500)
        }


    } //show mesage

    static logOut() {
        console.log(document.cookie = "_id= ; expires = Thu, 01 Jan 1970 00:00:00 GMT");
        location.reload();

    }
}

//____________________________________________________________-----_-___________________________

//view.html
const box = document.getElementById("box");
console.log(box);

box.onscroll = (e) => {
    var windowScroll = box.scrollTop;
    var windowHeight = box.scrollHeight - box.clientHeight;
    var scrollAmount = (windowScroll / windowHeight) * 100;
    document.getElementById("thumb").style.width = scrollAmount.toString() + "%";



}



class viewMeth {
    static fullscreen() {
        box.requestFullscreen().then(() => {
            let btn = document.getElementById("fulls");
            btn.innerHTML = " <span class='material-icons'>fullscreen_exit</span>";
        });
    }
    static printE() {
        console.log("print");

        print()
    }
}


//face book configurations
// window.fbAsyncInit = function() {
//     FB.init({
//       appId      : '{2589928161224931}',
//       cookie     : true,
//       xfbml      : true,
//       version    : '{api-version}'
//     });

//     FB.AppEvents.logPageView();   

//   };

//   (function(d, s, id){
//      var js, fjs = d.getElementsByTagName(s)[0];
//      if (d.getElementById(id)) {return;}
//      js = d.createElement(s); js.id = id;
//      js.src = "https://connect.facebook.net/en_US/sdk.js";
//      fjs.parentNode.insertBefore(js, fjs);
//    }(document, 'script', 'facebook-jssdk'));


//    FB.getLoginStatus(function(response) {
//     statusChangeCallback(response);
// });