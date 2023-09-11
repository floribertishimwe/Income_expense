const Alert = document.querySelector('.messages')
const btnClose=document.querySelector('.btn-close')
btnClose.addEventListener('click',()=>{
    Alert.style.display = 'none';
});