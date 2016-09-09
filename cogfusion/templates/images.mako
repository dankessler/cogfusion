<%inherit file="master.mako"/>


<h1>Labeled Images</h1>

<ol>
% for image in data:
    <li>${image}</li>
% endfor
</ol>



