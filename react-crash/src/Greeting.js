import React from 'react';

function Greeting() {
    const date = new Date();
    let timeDay;
    const styles = {
        fontSize: "24px",
        textAlign: "center"
    }

    if(date.getHours() < 12){
        timeDay = 'Morning';
        styles.color = "rgb(187, 184, 21)";
    }else if(date.getHours() >= 12 && date.getHours() < 17){
        timeDay = 'Afternoon';
        styles.color = "rgb(30, 56, 126)";
    }else{
        timeDay = 'Night';
        styles.color = "rgb(39, 38, 2)";
    }
    // const styles = {
    //     color: "#FF8C00",
    //     fontSize: "24px",
    //     textAlign: "center"
    // }

    return <div>
        <h2 style={styles}>Good {`${timeDay}, it's ${date.getHours() % 12} o'clock !!`}</h2>
        {/* JSX expects style to not be String but instead to be Obj => {} */}
        {/* change JSX to JS => wrap syntax in {} => style={{color: "#FF8C00"}} */}
    </div>
}
export default Greeting;