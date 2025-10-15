<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="html" indent="yes"/>

    <xsl:template match="/">
        <html>
            <head>
                <title>Books Table</title>
                <style>
                    table {border-collapse: collapse; width: 70%;}
                    th, td {border: 1px solid black; padding: 8px;}
                    th {background-color: #f2f2f2;}
                </style>
            </head>
            <body>
                <h2>All Books</h2>
                <table>
                    <tr>
                        <th>Book</th>
                        <th>ISBN</th>
                        <th>Title</th>
                        <th>Author</th>
                    </tr>
                    <xsl:for-each select="books/book">
                        <tr>
                            <td><xsl:value-of select="name()"/></td>
                            <td><xsl:value-of select="@isbn"/></td>
                            <td><xsl:value-of select="title"/></td>
                            <td><xsl:value-of select="author"/></td>
                        </tr>
                    </xsl:for-each>
                </table>

                <h2>Books with Price 100</h2>
                <ul>
                    <xsl:for-each select="books/book[price=100]">
                        <li>
                            <xsl:value-of select="title"/> by <xsl:value-of select="author"/>
                        </li>
                    </xsl:for-each>
                </ul>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
