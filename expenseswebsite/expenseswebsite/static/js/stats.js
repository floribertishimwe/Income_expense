
const renderChat=(data,labels)=>{
  var ctx = document.getElementById("myChart").getContext("2d");
  new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: labels,
        datasets: [{
          label: 'Last 6 months expenses',
          data: data,
          backgroundColor:[
              "rgba(255,99,132,0.8)",
              "rgba(54,162,235,0.8)",
              "rgba(255,206,86,0.8)",
              "rgba(75,192,192,0.8)",
              "rgba(153,102,255,0.8)",
              "rgba(255,159,64,0.8)",
  
          ],
  
          borderColor:[
              "rgba(255,99,132,1)",
              "rgba(54,162,235,1)",
              "rgba(255,206,86,1)",
              "rgba(75,192,192,1)",
              "rgba(153,102,255,1)",
              "rgba(255,159,64,1)",
          ],        
          borderWidth: 1
        }]
      },
      options: {
       title:{
          display:true,
          text:'Expenses per category',
       },
      },
    });



};
const getChartData=()=>{
  // console.log("fetching");
    fetch('/expense_category_summary')
    .then(res=>res.json())
    .then(results=>{
// console.log("results",results);
const category_data = results.expense_category_data;

const [labels,data] =[
Object.keys(category_data),
Object.values(category_data),
];
let sum=0
const data_percentage=[]
data.map((item)=>{
  sum+=item
})
data.map((single_data)=>{
  let perc=((single_data*100)/sum).toFixed(2)
  data_percentage.push(perc)
})

// console.log(sum);
console.log(data_percentage);

// // console.log(labels,data)
// console.log(data)

// // var total_data=0;
// // total_data+=data;
// // console.log("total_data",total_data);

renderChat(data,labels);

    });

};
document.onload = getChartData();
