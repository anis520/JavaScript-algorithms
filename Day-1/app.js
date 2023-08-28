
//For inputArray = [1, 2, 1], elementToReplace = 1 and subtractionElem = 3,
//the output should be arrayReplace(inputArray, elementToReplace, substrationElem) = [3, 2, 3].

function arrayReplace(inputArray,elementToReplace,substration){

  inputArray.forEach((item, i) => {

             if (item==elementToReplace) {
                 inputArray[i]=substration
             }

  });


  console.log(inputArray);


}


arrayReplace([1,2,1],1,3)
