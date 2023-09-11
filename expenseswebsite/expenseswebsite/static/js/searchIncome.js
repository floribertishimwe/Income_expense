const searchField = document.querySelector('#searchField');
const tableBody =document.querySelector('.table-body');
const tableOutput = document.querySelector('.table-output');
const appTable = document.querySelector('.app-table');
const paginationContainer = document.querySelector('.pagination-container');
tableOutput.style.display='none'

searchField.addEventListener('keyup',(e)=>{
const searchValue=e.target.value;
if(searchValue.trim().length > 0)
{
  paginationContainer.style.display="none";
  tableBody.innerHTML="";
  // console.log('searchValue',searchValue);

//   start of API

fetch("/search-income", {
    body: JSON.stringify({searchText:searchValue}),
    method:"POST",
})
.then( (res)=> res.json())
.then((data) => {

 
console.log("data",data);
appTable.style.display="none";
tableOutput.style.display="block";

if (data.length === 0){ 

    tableOutput.innerHTML ="No results found"
}else{
  data.forEach(item =>{

    tableBody.innerHTML +=`
    <tr>
    <td>${item.amount}</td>
    <td>${item.source}</td>
    <td>${item.description}</td>
    <td>${item.date}</td>

    </tr>`;
  });
}
});
// End of the ApI
}else{
  tableOutput.style.display="none";
  appTable.style.display="block";
  paginationContainer.style.display="block";
}
}); 