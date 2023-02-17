import React from 'react';
import '../../styles.scss'

function ButtonCustom(props) {
    return (
        <button className="button-container" onClick={props.onClick} style={props.style}>
            {props.title}
        </button>
    );
}
export default ButtonCustom;
