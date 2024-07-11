const username = document.getElementById("username");
const password = document.getElementById("password");
const myForm  = document.querySelector("#login-form");
const register_form = document.querySelector("#register-form");
const confirm_password = document.querySelector("#confirm_password");
const statusDIv = document.querySelector("#status")

// login handler
if(myForm){
myForm.addEventListener("submit", function(event) {

    event.preventDefault();

    if(username.value=='' && password.value=='') {
        alert("Please fill out both fields.");
        return;
    }
    const userObj = {
        username:username.value,
        password:password.value
    }
//jwt json web token
    axios.post('/login_user',userObj,{
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function(resp){
        if(resp.data.status==200){
            //todo: login is successfull redirect user to intended page
            console.log('Logged In Successfully')
            window.location.href = '/dashboard'
        }else{
            statusDIv.innerHTML=resp.data.message
            // alert(resp.data.message);
        }
        
    }).catch(function(err){
        console.error(err);
       
    })

})


}

// register handler
if (register_form){

    register_form.addEventListener("submit", function(event) {
        event.preventDefault();
        if(username.value=='' || password.value=='' || confirm_password.value=='') {
            alert("Please fill out both fields.");
            return;
        }
        if(password.value!== confirm_password.value){
            alert("Passwords do not match.");
            return;
        }
        const userObj = {
            username:username.value,
            password:password.value
        }
        // asynchronous - 
        axios.post('register_user', userObj,{
            headers: {
                'Content-Type': 'application/json'
            }
        }).then((response) => {
            if(response.data.status==200){
                //todo: registration is successfull redirect user to intended page
                console.log('Registered Successfully')
                window.location.href = '/'
            }else{
                statusDIv.innerHTML=response.data.message
                // alert(response.data.message);
            }
        }).catch((err) => {
            console.error(err);
            alert("An error occurred while registering. Please try again later.")
        })


    
    }) 

}
 



