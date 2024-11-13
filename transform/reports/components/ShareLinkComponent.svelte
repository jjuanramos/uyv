<script context="module">
    export const evidenceInclude = true;
</script>

<script lang="ts">
    import { generateShareLink } from './shareLink';
    export let xLabel = "date";
    export let yLabel = "value";
    export let xdata = [];
    export let dividerLines = [];
    export let lockedLimits = null;
    export let lockedLimitStatus = null;
    let shareLink;
    // Whenever any of the props change, this code will run
    $: {
        if (xLabel && yLabel && xdata) {
            shareLink = generateShareLink({xLabel, yLabel, xdata, dividerLines, lockedLimits, lockedLimitStatus});
        }
    }
</script>

<!-- You can use {shareLink} anywhere in your HTML now -->
<div>
    See <a href={shareLink} style="color: blue; text-decoration: underline;">XmR chart</a>
</div>