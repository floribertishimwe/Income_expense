var toggleBtn = document.querySelector('.toggle_btn')
var toggleBtnIcon= document.querySelector('.toggle_btn i')
var dropDownMenu = document.querySelector('.dropdown_menu')
toggleBtn.addEventListener("click",()=>{
    dropDownMenu.classList.toggle('open');
    const isOpen = dropDownMenu.classList.contains('open');
    toggleBtnIcon.classList = isOpen 
    ?'fa-solid fa-xmark'
    :'fa-solid fa-bars'
})
document.querySelectorAll('.nav-item').forEach(n =>
    n.addEventListener('click',()=>{
    dropDownMenu.classList.remove('open');
    toggleBtnIcon.classList = 'fa-solid fa-bars';
    }))

