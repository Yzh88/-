//封装函数，获取元素节点


function $(tag,index){
     var elems = document.getElementsByTagName(tag);

     //判断index是否存在
     if (index){
          //iindex为非零下标
        return elems[index];
     }else{//index==0或index==undefined
        return elems[0];

     }
}

//$('h1') 参数index 省略，默认为undefined