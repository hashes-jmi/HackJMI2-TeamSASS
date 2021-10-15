import React from 'react'
import { useState ,useRef} from 'react'
import Input from '../UI/Input/Input'
import Button from '../UI/Buttons/Button'
function UserMedicalData(){
const [userData,setUserData]=useState({'height':'','weight':'','blood_group':'','allergiers':[],'surgery':[],'disease':[]})
const [listCount,setListCount]=useState({'allergiers':0,'surgery':0})
const addNewInput=(text,node)=>{
    setListCount((prev)=>{return {...prev,allergiers:prev.allergiers+1}})
    const handler=(e)=>{console.log(e.target.value)};
    node.insertAdjacentHTML('beforebegin',`
    <div>
        
        <Input id=${"user-"+text+"-"+listCount.allergiers} type="text"> 
        </div>`)
    
}
{/* <label htmlFor=${"user-"+text+"-"+userData[text].length}>${text}</label> */}
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
        <label htmlFor="user-allergiers">Your Allergers</label>
        <div>
        
        {/* <Input
        id={"user-allergiers-"+userData.allergiers.length+1}
        type="text"
        placeholder="Enter your allerge"
        onChange={(e)=>{console.log(e.target.value)}}
        /> */}
        <Button onClick={(e)=>{ addNewInput("allergiers",e.target);}}>Add</Button>
        </div>
        
        
    </div>
    <div>
        <label htmlFor="user-surgery">Your surgeries</label>
        <div>
        
        {/* <Input
        id={"user-allergiers-"+userData.allergiers.length+1}
        type="text"
        placeholder="Enter your allerge"
        onChange={(e)=>{console.log(e.target.value)}}
        /> */}
        <Button onClick={(e)=>{ addNewInput("surgery",e.target);}}>Add</Button>
        </div>
        
        
    </div>
    <div>
        <label htmlFor="user-disease">Your Disease</label>
        <div>
        
        {/* <Input
        id={"user-allergiers-"+userData.allergiers.length+1}
        type="text"
        placeholder="Enter your allerge"
        onChange={(e)=>{console.log(e.target.value)}}
        /> */}
        <Button onClick={(e)=>{ addNewInput("disease",e.target);}}>Add</Button>
        </div>
        
        
    </div>
    <Button>Submit Data</Button>
</form>
</>
)

}

export default UserMedicalData;