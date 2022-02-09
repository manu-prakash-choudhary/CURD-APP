const backBtn = document.getElementById('back-btn')
const alerBox = document.getElementById('alert-box')

const url = window.location.href + '\data'
const updateUrl = window.location.href + 'update/'
const deleteUrl = window.location.href + 'delete/'

const updateForm = document.getElementById('update-form')
const deleteForm = document.getElementById('delete-form')

const spinnerBox = document.getElementById('spinner-box')
const updateBtn = document.getElementById("update-btn")
const deleteBtn = document.getElementById("delete-btn")
const postBox = document.getElementById('post-box')
const titleInput = document.getElementById("id_title")
const bodyInput = document.getElementById('id_body')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const alertBox = document.getElementById('alert-box')

backBtn.addEventListener('click', () => {
    history.back()
})
 
$.ajax({
    type:'GET',
    url: url,
    success: function (response) {
        console.log(response)
        data = response.data
        spinnerBox.classList.add('not-visible')
        if (data.author == data.logged_in) {
            console.log("Its same")
            updateBtn.classList.remove("not-visible")
            deleteBtn.classList.remove("not-visible")
        }
        else {
            console.log("Its not same")
        }
        const titleEl = document.createElement("h3")
        titleEl.setAttribute('class', 'mt-1')
        titleEl.setAttribute('id','title')
        
        const bodyEl = document.createElement("p")
        bodyEl.setAttribute('class', 'mt-1');
        bodyEl.setAttribute('id','body')
        

        titleInput.value = data.title
        bodyInput.value = data.body
        titleEl.textContent = data.title;
        bodyEl.textContent = data.body;
        
        console.log("titleEl : " + titleEl.textContent)
        console.log("bodyEl : " + bodyEl.textContent)
        postBox.appendChild(titleEl);
        postBox.appendChild(bodyEl);

    },
    error: function (response) {
        console.log(response)
    }
    
})

updateForm.addEventListener('submit', e => {
    e.preventDefault()
    title = document.getElementById('title')
    body = document.getElementById('body')

    $.ajax({
        'type': 'POST',
        'url': updateUrl,
        'data': {
            'csrfmiddlewaretoken' : csrf[0].value,
            'title': titleInput.value,
            'body': bodyInput.value,
        },
        success: function (response) {
            console.log(response)
            handleAlerts('success','post has been updated succesfully')
            title.textContent = response.title;
            body.textContent = response.body;

        },
        error: function (response) {
            console.log(error)
            handleAlerts('error','oops something went wrong')
        }
        
    })

} )

deleteForm.addEventListener('submit', e => {
    e.preventDefault(),
        $.ajax({
            type : 'POST',
            "url": deleteUrl,
            data: {
                csrfmiddlewaretoken: csrf[0].value,
            },
            success: function (response) {
                window.location.href = window.location.origin
                localStorage.setItem('title',titleInput.value)
            },
            error: function (response) {
                console.log(response)
            }
            
            
        })
        
        
        
    
})