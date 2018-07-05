var readline=require('readline');
var rl=readline.createInterface({input:process.stdin,
  output:process.stdout});
rl.question('enter number:',function(n){
  var a=parseInt(n);
  function fact(a)
  {
    if(a==0)
    {
      return 1;
    }
    return a*fact(a-1);
  }
  console.log('factorial of number is:');
  console.log(fact(a));
});