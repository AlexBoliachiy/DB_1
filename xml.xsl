<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">


<html xmlns="http://www.w3.org/1999/xhtml">
  <body>
  <h2>Ноутбуки</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th>Название</th>
      <th>Фото</th>
        <th>Цена</th>
    </tr>
    <xsl:for-each select="Notebooks/Notebook">
    <tr>
        <td>
       <img>
        <xsl:attribute name="src">
       <xsl:value-of select='src'/>
        </xsl:attribute>
       </img>
         </td>
       <td><xsl:value-of select="name"/></td>

        <td><xsl:value-of select="worth"/></td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>

</xsl:stylesheet>