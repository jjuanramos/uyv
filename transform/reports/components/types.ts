export interface XData {
    x: string, // date in yyyy-mm-dd
    value: number
}

export interface DividerLines {
    id: string,
    x: number // date in unix milliseconds
}

export interface LockedLimits {
    avgX: number,
    avgMovement: number,
    UNPL: number, // upper natural process limit
    LNPL: number, // lower natural process limit
    URL: number, // upper range limit
}

export interface ShareLinkParams {
    xLabel: string,
    yLabel: string,
    xdata: XData[],
    dividerLines?: DividerLines[],
    lockedLimits?: LockedLimits,
    lockedLimitStatus?: number,
}