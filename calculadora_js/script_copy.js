const calculator = document.querySelector('.calculator')
const keys = calculator.querySelector('.calculador__keys')

keys.addEventListener('click', e =>{
    if(e.target.matches('button')) {  
        const key = e.matches('button')
        const action = key.dataset.action

        if(!action){
            console.log('number key!')
        }
        if(action === 'calculate'){
            const sencondValeu = displayedNum
            if (action === 'add' ||
                action === 'subtract' ||
                action === 'multiply' ||
                action === 'divide'
            ){
                console.log("operador key!")
                /*calculator.dataset.firstValue = displayedNum
                calculator.dataset.operator = action
                if(action === 'calculate'){
                    const firstValue = calculator.dataset.firstValue
                    const operador = calculator.dataset.operador
                    const secondValue = displayedNum

                    display.textContent = calculate(firstValue, operator, secondValue)
                */}
            if (action === "decimal"){
                console.log("decimal key!");
            }
            if (action === "clear") {
                console.log("clear key!");
            }
            if (action === "calculate") {
                console.log(("equal key"));
            }
            }
        }
        
    }
)

