<?php

function setTitle($title = null) {
    echo "<title>" . htmlspecialchars($title) . "</title>";
}

function setDescription($description = null) {
    echo '<meta name="description" content="' . htmlspecialchars($description) . '">';
}

function setKeywords($keywords = null) {
    echo '<meta name="keywords" content="' . htmlspecialchars($keywords) . '">';
}

?>
