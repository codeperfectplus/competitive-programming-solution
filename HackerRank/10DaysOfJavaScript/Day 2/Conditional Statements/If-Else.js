function getGrade(score) {
    let grade;
    // Write your code here
    if(score<=5) {
        grade="F";
    }else if(score<=10) {
        grade='E';
    }else if(score<=15) {
        grade='D'
    }else if(score<=20) {
        grade ='C'
    }else if(score<=25) {
        grade ='B'
    }else if(score<=30) {
        grade='A'
    }
    return grade;
}
