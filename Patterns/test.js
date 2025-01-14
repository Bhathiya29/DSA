function multiply(...args){
  return args.reduce((accumulator,currentValue)=>accumulator*currentValue,0)
}