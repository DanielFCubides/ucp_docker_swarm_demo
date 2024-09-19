'use client'

import {useEffect, useState} from "react";

export const Counter = ({initialValue = 0, targetValue = 0}) => {
    const duration = 200;
    const [count, setCount] = useState(initialValue);

    useEffect(() => {
        let startValue = initialValue;
        const interval = Math.floor(
            duration / (targetValue - initialValue));

        const counter = setInterval(() => {
            startValue += 1;
            setCount(startValue);
            if (startValue >= targetValue) {
                clearInterval(counter);
            }
        }, interval);

        return () => {
            clearInterval(counter);
        };
    }, [targetValue, initialValue]);
    return (
        <>{count}</>
    )
}
