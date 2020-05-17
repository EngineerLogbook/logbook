new SimpleMDE({
    autofocus: true,
    element: document.getElementById("logcontent"),
    spellChecker: false,
    lineWrapping: true,
    placeholder: "Type here...",
    hideIcons: ['side-by-side'],
    shortcuts: {
        drawTable: "Cmd-Alt-T"
    },
    autoDownloadFontAwesome: true,
});