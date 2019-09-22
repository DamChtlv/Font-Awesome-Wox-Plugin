const fs        = require('pn/fs')
const svg2png   = require('svg2png')

function jsonReader(filePath, cb) {
    fs.readFile(filePath, (err, fileData) => {
        if (err) {
            return cb && cb(err)
        }
        try {
            const object = JSON.parse(fileData)
            return cb && cb(null, object)
        } catch(err) {
            return cb && cb(err)
        }
    })
}

jsonReader('./Json/icons.json', (err, iconsData) => {

    if (err)
        return console.log(err)

    let i = 0
    const iconPath = 'Images/Icons/';

    for (let iconName in iconsData) {

        /** Skip existing icons */
        if (fs.existsSync(iconPath + iconName + '.png'))
            continue;

        i++

        const iconData  = iconsData[iconName];
        const iconStyle = iconData.styles[0];
        let iconSVG     = iconData.svg[iconStyle].raw;

        /** Add color of Font Awesome to icons to make them visible for white / dark Wox UI */
        iconSVG         = iconSVG.replace(/<path/i, '<path fill="#4dabf7"')

        const output = svg2png.sync(iconSVG, { width: 40, height: 40, filename: `${iconPath}${iconName}.png` })
        try {
            fs.writeFileSync(`${iconPath}${iconName}.png`, output, { flag: "wx" });
            console.log(iconName + '.png created!');
        }
        catch (err) {
            return console.error(err)
        }
    }

    return false;
})