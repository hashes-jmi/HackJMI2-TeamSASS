const form=document.getElementById("signupForm")

form.onsubmit=(e)=>{
    e.preventDefault();
    let userData={
        "name":document.getElementById("create-first-name").value+" "+document.getElementById("create-last-name").value,
        "address":{
            "line1":document.getElementById("create-address-line1").value,
            "country":document.getElementById("create-address-country").value,
            "state":document.getElementById("state").value,
            "pincode":document.getElementById("create-address-pincode").value
        },
        "phone":document.getElementById("create-phone-number").value,
        "email":document.getElementById("create-email").value,
        "aadhar":document.getElementById("create-aadhaar").value,
    }
    axios.post("https://mhodsaifansari.pythonanywhere.com/register",userData)
    .then((response)=>{
        console.log(response.data);
        localStorage.setItem('eid',response.data.eid);
        location.href="verify.html"
    })
    .catch((err)=>{
        console.log(err);
    })
    console.log(userData)
}
