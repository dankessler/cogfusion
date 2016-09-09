<%inherit file="master.mako"/>


<h1>${contrast['contrast_text']}</h1>

        <ul>
<%
    matches = conceptsByContrasts[conceptsByContrasts['contrast']==contrastid]
%>
% for index, row in matches.iterrows():

<%
    concept = concepts[concepts['id']==row['concept']].iloc[0]
%>
            <li>${concept['name']}</li>
% endfor
        </ul>
