import React from 'react'
import { useState ,useRef} from 'react'
import Input from '../UI/Input/Input'
import Button from '../UI/Buttons/Button'
function UserMedicalData(){
const [userData,setUserData]=useState({'height':'','weight':'','blood_group':'','allergiers':[],'surgery':[],'disease':[]})

const addNewInput=(text)=>{
    
    <div>
        <label htmlFor={"user-"+text+"-"+userData[text].length}>{text}</label>
    <Input
    id={"user-"+text+"-"+userData[text].length}
    type="text"
    onChange={(e)=>{console.log(e.target.value)}}
    />
    </div>
    
}

return (
<>
<form onSubmit={(e)=>{e.preventDefault()}}>
    <div>
      <label htmlFor="user-height">Height</label>
       <Input 
        id='user-height'
        type="tel"
        placeholder="Enter Your height in centimeter"
        onChange={(e)=>{console.log(e.target.value)}}
        maxLength="3"
       />     
    </div>
    <div>
        <label htmlFor="user-weight">Weight</label>
        <Input
        id="user-weight"
        type="tel"
        placeholder="Enter your weight in Kilogram"
        onChange={(e)=>{console.log(e.target.value)}}
        />
    </div>
    <div>
        <label htmlFor="user-blood-group">Enter User's Blood Group</label>
        <Input
        id="user-blood-group"
        type="text"
        placeholder="Enter your blood group"
        onChange={(e)=>{console.log(e.target.value)}}
        maxLength="4"
        />
    </div>
    <div>
        <div>
        <label htmlFor="user-allergiers">Your Allergers</label>
        <Input
        id={"user-allergiers-"+userData.allergiers.length+1}
        type="text"
        placeholder="Enter your allerge"
        onChange={(e)=>{console.log(e.target.value)}}
        />
        </div>
        <Button onClick={(e)=>{addNewInput()}}></Button>
        <button onClick={(e)=>{ addNewInput("allergiers",e);}}>Add</button>
    </div>
   
</form>
</>
)

}

export default UserMedicalData;