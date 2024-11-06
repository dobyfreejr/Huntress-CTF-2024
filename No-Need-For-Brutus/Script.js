function caesarCipherDecrypt(str, shift) {
    const alphabet = 'abcdefghijklmnopqrstuvwxyz';
    let decrypted = '';

    for (let char of str) {
        if (alphabet.includes(char)) {
            let index = (alphabet.indexOf(char) - shift + 26) % 26; // Adjust for negative shifts
            decrypted += alphabet[index];
        } else {
            decrypted += char; // Non-alphabet characters remain the same
        }
    }

    return decrypted;
}

// Try different shifts (1-25) to see if we can find a meaningful message
for (let shift = 1; shift < 26; shift++) {
    const decrypted = caesarCipherDecrypt('squiqhyiiycfbudeduutvehrhkjki', shift);
    console.log(`Shift ${shift}: ${decrypted}`)