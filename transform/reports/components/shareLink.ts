import { XData, DividerLines, LockedLimits, ShareLinkParams } from './types';
import lz77 from "lz77";

export function generateShareLink(s: ShareLinkParams): string {
    const paramsObj = {
        v: "0" // version
    };
    let validXdata = s.xdata.filter(dv => dv.x || dv.value)
    const dateText = `${s.xLabel ? s.xLabel.replace(",", ";") : ''},${s.yLabel ? s.yLabel.replace(",", ";") : ''},` +
        validXdata.map((d) => {
            if (d.x) {
                return d.x.replace(",", ";")
            } else {
                return ''
            }
        }).join(",")
    const valueText = validXdata.map((d) => d.value)
    paramsObj['d'] = btoaUrlSafe(lz77.compress(dateText)) + '.' +
        encodeNumberArrayString(valueText)
    if (s.dividerLines) {
        const dividers = encodeNumberArrayString(s.dividerLines.map(dl => dl.x))
        if (dividers.length > 0) {
            paramsObj['s'] = dividers
        }
    }
    if (s.lockedLimits && (s.lockedLimitStatus ?? 0 & 1) == 1) {
        paramsObj['l'] = encodeNumberArrayString([
            s.lockedLimits.avgX,
            s.lockedLimits.avgMovement,
            s.lockedLimits.LNPL,
            s.lockedLimits.UNPL,
            s.lockedLimits.URL,
            s.lockedLimitStatus ?? 0
        ])
    }
    const searchParams = new URLSearchParams(paramsObj);
    const fullPath = `https://xmrit.com/t/?${searchParams.toString()}`
    return fullPath
}

export function encodeNumberArrayString(input: number[]): string {
    const buffer = new ArrayBuffer(input.length * 4);
    const view = new DataView(buffer);
    input.forEach((i, idx) => {
        view.setFloat32(idx * 4, i)
    })
    return btoaUrlSafe(
        new Uint8Array(buffer)
            .reduce((data, byte) => data + String.fromCharCode(byte), '')
    )
}

export function btoaUrlSafe(s: string): string {
    return btoa(s).replace(/\+/g, '-').replace(/\//g, '_').replace(/=/g, '')
}