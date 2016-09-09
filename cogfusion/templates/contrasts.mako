<%inherit file="master.mako"/>


<h1>Contrasts</h1>

<ul>
% for index, contrast in contrasts.iterrows():
    <li>
        ${contrast['contrast_text']}
        <ul>
<%
    matches = conceptsByContrasts[conceptsByContrasts['contrast']==contrast['id']]
%>
% for index, row in matches.iterrows():

<%
    concept = concepts[concepts['id']==row['concept']].iloc[0]
%>
            <li>${concept['name']}</li>
% endfor
        </ul>
    </li>
% endfor
</ul>



